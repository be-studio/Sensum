import { useState, createContext, PropsWithChildren } from "react";
import { useCsrfQuery } from "../hooks/useCsrfQuery";

interface AuthContextInterface {
  user: any;
  login: (user: string, callback: VoidFunction) => void;
  logout: (callback: VoidFunction) => void;
}

export const AuthContext = createContext<AuthContextInterface | null>(null);

export const AuthProvider = ({ children }: PropsWithChildren) => {
  const [user, setUser] = useState<any>(null);

  //const {} = useCsrfQuery();

  const login = (user: string, callback: VoidFunction) => {

  };

  const logout = (callback: VoidFunction) => {

  };

  return <AuthContext.Provider value={{ user, login, logout }}>{children}</AuthContext.Provider>;
};
