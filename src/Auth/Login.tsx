import { useState, ChangeEvent, FormEvent, useEffect } from "react";

import { useLoginMutation } from "./hooks/useLoginMutation";
import { useUsersQuery } from "../User/hooks/useUsersQuery";
import { useAuth } from "./hooks/useAuth";
import { useNavigate } from "react-router-dom";


export const Login = () => {
  const auth = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [csrf, setCsrf] = useState("");
  const navigate = useNavigate();

  const { data, mutateAsync } = useLoginMutation(username, password);
  const { data: users } = useUsersQuery();

  useEffect(() => {
    if(data && data.access) {
      localStorage.setItem("sensum-access", data.access);
      navigate("/user");
    }
  }, [data]);

  const handleChangeUsername = ({ target }: ChangeEvent<HTMLInputElement>) => {
    setUsername(target.value);
  }

  const handleChangePassword = ({ target }: ChangeEvent<HTMLInputElement>) => {
    setPassword(target.value);
  }

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    mutateAsync()
    .then(() => {
      console.log('noo');
      auth.login("user");
    });
  };

  return (
    <>
      <h1>Login</h1>

      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username</label>
        <input name="username" type="text" value={username} onChange={handleChangeUsername} />

        <label htmlFor="password">Password</label>
        <input name="password" type="password" value={password} onChange={handleChangePassword} />

        <button type="submit">Login</button>
      </form>
    </>
  );
};
