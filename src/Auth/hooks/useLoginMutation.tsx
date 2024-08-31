import { useMutation } from "react-query";
import getCookie from "../../utility/auth/getCookie";
import { api } from "../../utility/auth/api";


export const useLoginMutation = (email: string, password: string) => {
  return useMutation({
    mutationKey: 'login',
    mutationFn: () => api.post("/login", {
        email,
        password
      }, {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        [import.meta.env.VITE_CSRF_TX]: getCookie(import.meta.env.VITE_CSRF_RX)
      },
    })
    .then((response) => {
      return response?.data;
    })
    .catch((error) => Promise.reject(error.response?.data)),
    onSuccess: (data) => console.log('Data', data),
    onError: (error) => console.log('Error', error),
    }
  )
};
