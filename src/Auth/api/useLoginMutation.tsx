import { useMutation } from "react-query";
import axios from "axios";

function getCookie(key: string) {
  var b = document.cookie.match("(^|;)\\s*" + key + "\\s*=\\s*([^;]+)");
  return b ? b.pop() : "";
}

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
        'X-CSRFToken': getCookie('csrftoken')
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
