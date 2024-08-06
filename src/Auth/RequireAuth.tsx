import { PropsWithChildren } from "react";
import { useAuth } from "./hooks/useAuth";
import { useLocation, Navigate, useNavigate } from "react-router-dom";
import { isExpired, decodeToken } from "react-jwt";
import { useJwtRefreshMutation } from "./hooks/useJwtRefreshMutation";


const navigateToLogin = <Navigate to="/login" />;

export const RequireAuth = ({ children }: PropsWithChildren) => {
  const auth = useAuth();
  const location = useLocation();
  const navigate = useNavigate();

  const { mutateAsync } = useJwtRefreshMutation();

  const jwt = localStorage.getItem("sensum-access");

  if(!jwt) {
    return navigateToLogin;
  }

  if(isExpired(jwt)) {
    mutateAsync().then(response => {
      localStorage.setItem("sensum-access", response.access);
      return (<>{children}</>);
    })
    .catch(() => {
      localStorage.removeItem("sensum-access");
      navigate("/login");
    });
  } else {
    return (<>{children}</>);
  }
};
