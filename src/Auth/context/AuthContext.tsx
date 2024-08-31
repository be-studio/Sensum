import { useState, createContext, PropsWithChildren } from "react";
import { useCsrfQuery } from "../hooks/useCsrfQuery";

interface AuthContextInterface {
  user: number;
  setUser: (id: number) => void;
}

export const AuthContext = createContext<AuthContextInterface>({
  user: 0,
  setUser: (id: number) => {}
});

export const AuthProvider = ({ children }: PropsWithChildren) => {
  const [user, setUser] = useState(0);

  return <AuthContext.Provider value={{ user, setUser }}>{children}</AuthContext.Provider>;
};
