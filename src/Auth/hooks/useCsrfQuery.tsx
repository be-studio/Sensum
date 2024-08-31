import { useQuery } from "react-query";
import axios from "axios";
import { api } from "../../utility/auth/api";


export const useCsrfQuery = () => {
  return useQuery(['get_csrf'], () => api.get("http://localhost:8000/get-csrf")
    .then((response) => response.data)
    .catch((error) => error.response), {
    cacheTime: 0,
    staleTime: 0,
  });
};
