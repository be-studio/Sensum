import { useUserQuery } from "./hooks/useUserQuery";
import { useLogoutMutation } from "../Auth/hooks/useLogoutMutation";
import { useNavigate } from "react-router-dom";


export const User = () => {
  const { data: user } = useUserQuery();
  const { mutateAsync: logout, isSuccess, isError } = useLogoutMutation();
  const navigate = useNavigate();

  const handleLogout = async() => {
    logout()
    .then(() => {
      navigate("/login");
    })
    .catch(() => {
      console.log("Unable to logout");
    })
  };

  return (
    <>
      <button onClick={handleLogout}>Logout</button>

      <h1>User</h1>

      {user && (
        <ul>
          <li>{user.first_name}</li>
        </ul>
      )}
    </>
  );
};
