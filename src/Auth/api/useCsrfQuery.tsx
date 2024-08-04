import { useQuery } from "react-query";
import axios from "axios";

export const useCsrfQuery = () => {
  return useQuery({
    //queryKey: ['get_csrf'],
    queryFn: () => axios.get("http://localhost:8000/get-csrf", {
      headers: {
        "Content-Type": "application/json",
      }
    })
    .then((response) => response.data)
    .catch((error) => error.response)
  });
};
