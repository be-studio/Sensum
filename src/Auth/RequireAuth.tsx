import { PropsWithChildren, useEffect, useState } from "react";
import { useAuth } from "./hooks/useAuth";
import { useLocation, Navigate, useNavigate } from "react-router-dom";
import { useRefreshJwtMutation } from "./hooks/useRefreshJwtMutation";
import { useVerifyJwtMutation } from "./hooks/useVerifyJwtMutation";


const navigateToLogin = <Navigate to="/login" />;

export const RequireAuth = ({ children }: PropsWithChildren) => {
  const auth = useAuth();
  const location = useLocation();
  const navigate = useNavigate();

  const { mutateAsync: refreshJwt } = useRefreshJwtMutation();
  const { mutateAsync: verifyJwt } = useVerifyJwtMutation();

  const jwt = sessionStorage.getItem("sensum-access");
  const [isJwtChecked, setIsJwtChecked] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    if(!jwt) {
      setIsAuthenticated(false);
      setIsJwtChecked(true);
    }

    verifyJwt()
    .then(() => {
      setIsAuthenticated(true);
      setIsJwtChecked(true);
    })
    .catch(() => {
      refreshJwt()
      .then(response => {
        sessionStorage.setItem("sensum-access", response.access);
        setIsAuthenticated(true);
        setIsJwtChecked(true);
      })
      .catch(() => {
        sessionStorage.removeItem("sensum-access");
        setIsAuthenticated(false);
        setIsJwtChecked(true);
      })
    })
  }, []);

  if(!isJwtChecked) {
    return <></>;
  }

  return isAuthenticated ? <>{children}</> : navigateToLogin;
};
