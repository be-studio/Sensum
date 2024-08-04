import { useState, ChangeEvent, FormEvent } from "react";

import { useCsrfQuery } from "./hooks/useCsrfQuery";
import { useLoginMutation } from "./hooks/useLoginMutation";

export const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [csrf, setCsrf] = useState("");

  const { data } = useCsrfQuery();
  const { mutateAsync } = useLoginMutation(username, password);

  const handleChangeUsername = ({ target }: ChangeEvent<HTMLInputElement>) => {
    setUsername(target.value);
  }

  const handleChangePassword = ({ target }: ChangeEvent<HTMLInputElement>) => {
    setPassword(target.value);
  }

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    mutateAsync();
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
