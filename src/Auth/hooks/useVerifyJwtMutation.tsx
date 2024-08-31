import { useMutation } from "react-query";
import { api } from "../../utility/auth/api";
import getCookie from "../../utility/auth/getCookie";


export const useVerifyJwtMutation = () => {
  return useMutation({
    mutationKey: 'verify-jwt',
    mutationFn: () => api.post("/verify-jwt", {
      token: sessionStorage.getItem("sensum-access"),
    }, {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        [import.meta.env.VITE_CSRF_TX]: getCookie(import.meta.env.VITE_CSRF_RX)
      },
      withCredentials: true,
    })
  });
};
