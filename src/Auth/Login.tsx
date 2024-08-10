import { useState, ChangeEvent, FormEvent, useEffect } from "react";

import { useLoginMutation } from "./hooks/useLoginMutation";
import { useAuth } from "./hooks/useAuth";
import { useNavigate } from "react-router-dom";


export const Login = () => {
  const auth = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [csrf, setCsrf] = useState("");
  const navigate = useNavigate();

  const { data, mutateAsync } = useLoginMutation(email, password);

  useEffect(() => {
    if(data && data.access) {
      sessionStorage.setItem("sensum-access", data.access);
      navigate("/user");
    }
  }, [data]);

  const handleChangeEmail = ({ target }: ChangeEvent<HTMLInputElement>) => {
    setEmail(target.value);
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
        <label htmlFor="email">Email Address</label>
        <input name="email" type="text" value={email} onChange={handleChangeEmail} />

        <label htmlFor="password">Password</label>
        <input name="password" type="password" value={password} onChange={handleChangePassword} />

        <button type="submit">Login</button>
      </form>
    </>
  );
};
