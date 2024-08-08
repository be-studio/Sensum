import { useUsersQuery } from "./hooks/useUsersQuery";
import { useLogoutMutation } from "../Auth/hooks/useLogoutMutation";
import { useNavigate } from "react-router-dom";


export const User = () => {
  const { data: users } = useUsersQuery();
  const { mutateAsync: logout, isSuccess, isError } = useLogoutMutation();
  const navigate = useNavigate();

  const handleLogout = async() => {
    logout()
    .then(() => {
      navigate("/login");
    })
    .catch(() => {
      alert("Unable to logout");
    })
  };

  return (
    <>
      <button onClick={handleLogout}>Logout</button>

      <h1>User</h1>
    </>
  );
};
