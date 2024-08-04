import { useMutation } from "react-query";
import axios from "axios";
import getCookie from "../../utility/auth/getCookie";

export const useLoginMutation = (username: string, password: string) => {
  return useMutation({
    mutationKey: 'login',
    mutationFn: () => axios.post("http://localhost:8000/login", {
        username,
        password
      }, {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        [import.meta.env.VITE_CSRF_TX]: getCookie(import.meta.env.VITE_CSRF_RX)
      },
      withCredentials: true
    })
    .then((response) => response?.data)
    .catch((error) => Promise.reject(error.response?.data)),
    onSuccess: (data) => console.log('Data', data),
    onError: (error) => console.log('Error', error),
    }
  )
};
