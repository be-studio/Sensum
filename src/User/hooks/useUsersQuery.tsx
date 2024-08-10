import { useQuery } from "react-query";
import { api } from "../../utility/auth/api";


export const useUsersQuery = () => {
  return useQuery({
    queryKey: ['users'],
    queryFn: () => api.get("/users", {
      headers: {
        Authorization: `Bearer ${sessionStorage.getItem("sensum-access")}`
      }
    })
    .then(response => response?.data)
    .then(data => data.json())
    .catch(error => console.log("Error getting users"))
  });
};
