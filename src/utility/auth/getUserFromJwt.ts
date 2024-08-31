import { decodeToken } from "react-jwt";

interface JwtClaims {
  user_id: number
}

export const getUserFromJwt = (token: string) => {
  const decodedToken: JwtClaims | null = decodeToken(token);

  return decodedToken?.user_id;
};
