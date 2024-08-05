import { PropsWithChildren } from "react";
import { useAuth } from "./hooks/useAuth";
import { useLocation, Navigate } from "react-router-dom";

export const RequireAuth = ({ children }: PropsWithChildren) => {
  const auth = useAuth();
  const location = useLocation();

  if(auth && !auth.user) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return (<>{children}</>);
};
