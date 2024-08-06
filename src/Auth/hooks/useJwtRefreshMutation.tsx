import { useMutation } from "react-query";
import { api } from "../../utility/auth/api";
import getCookie from "../../utility/auth/getCookie";


export const useJwtRefreshMutation = () => {
  return useMutation({
    mutationKey: 'jwt-refresh',
    mutationFn: () => api.post("/refresh-alt", { }, {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        [import.meta.env.VITE_CSRF_TX]: getCookie(import.meta.env.VITE_CSRF_RX)
      },
      withCredentials: true,
    })
    .then(response => response?.data)
    .catch(error => console.log(error)),
  });
};
