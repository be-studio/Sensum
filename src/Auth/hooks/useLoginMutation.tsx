import { useMutation } from "react-query";
import axios from "axios";
import getCookie from "../../utility/auth/getCookie";
import { api } from "../../utility/auth/api";


export const useLoginMutation = (username: string, password: string) => {
  console.log(getCookie(import.meta.env.VITE_CSRF_RX));
  return useMutation({
    mutationKey: 'login',
    mutationFn: () => api.post("http://localhost:8000/login", {
        username,
        password
      }, {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        [import.meta.env.VITE_CSRF_TX]: getCookie(import.meta.env.VITE_CSRF_RX)
      },
    })
    .then((response) => response?.data)
    .catch((error) => Promise.reject(error.response?.data)),
    onSuccess: (data) => console.log('Data', data),
    onError: (error) => console.log('Error', error),
    }
  )
};
