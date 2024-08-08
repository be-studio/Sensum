import { useMutation } from "react-query";
import getCookie from "../../utility/auth/getCookie";
import { api } from "../../utility/auth/api";
import { useCookies } from "react-cookie";

export const useLogoutMutation = () => {
  const [_, __, removeCookie] = useCookies();

  return useMutation({
      mutationKey: 'logout',
      mutationFn: () => api.post("/logout", {}, {
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${localStorage.getItem("sensum-access")}`,
          "Content-Type": "application/json",
          [import.meta.env.VITE_CSRF_TX]: getCookie(import.meta.env.VITE_CSRF_RX)
        },
      })
      .then((response) => {
        return response?.data;
      })
      .catch((error) => Promise.reject(error.response?.data)),
      onSuccess: (data) => {
        console.log("logged out");
        localStorage.removeItem("sensum-access");
      },
      onError: (error) => console.log('Error', error),
    }
  )
};
