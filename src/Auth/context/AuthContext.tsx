import { useState, createContext, PropsWithChildren } from "react";
import { useCsrfQuery } from "../hooks/useCsrfQuery";

interface AuthContextInterface {
  user: any;
  login: (user: string, callback?: VoidFunction) => void;
  logout: (callback: VoidFunction) => void;
}

export const AuthContext = createContext<AuthContextInterface>({
  user: null,
  login: () => {},
  logout: () => {}
});

export const AuthProvider = ({ children }: PropsWithChildren) => {
  const [user, setUser] = useState<any>(null);

  const login = (user: string, callback?: VoidFunction) => {
    console.log('what');
    console.log(user);
    setUser(user);
  };

  const logout = (callback: VoidFunction) => {

  };

  return <AuthContext.Provider value={{ user, login, logout }}>{children}</AuthContext.Provider>;
};
