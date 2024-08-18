import { useQuery } from "react-query";
import { api } from "../../utility/auth/api";
import { getUserFromJwt } from "../../utility/auth/getUserFromJwt";


export const useUserQuery = () => {
  const token = sessionStorage.getItem("sensum-access");

  if(!token) {
    throw new Error("Unable to get user");
  }

  return useQuery({
    queryKey: ['user'],
    queryFn: () => api.get(`/api/user/${getUserFromJwt(token)}`, {
      headers: {
        Authorization: `Bearer ${sessionStorage.getItem("sensum-access")}`
      }
    })
    .then(response => response?.data)
    //.then(data => data.json)
    .catch(error => console.log("Error getting the user" + error))
  });
};
