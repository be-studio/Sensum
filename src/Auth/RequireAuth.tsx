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

  const { mutateAsync } = useRefreshJwtMutation();
  const { mutateAsync: verifyJwt } = useVerifyJwtMutation();

  const jwt = sessionStorage.getItem("sensum-access");
  const [isJwtVerified, setIsJwtVerified] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    if(!jwt) {
      setIsAuthenticated(false);
      setIsJwtVerified(true);
    }

    verifyJwt()
    .then(() => {
      setIsAuthenticated(true);
      setIsJwtVerified(true);
    })
    .catch(() => {
      sessionStorage.removeItem("sensum-access");
      setIsAuthenticated(false);
      setIsJwtVerified(true);
    })
  }, []);

  if(!isJwtVerified) {
    return <></>;
  }

  return isAuthenticated ? <>{children}</> : navigateToLogin;
};
