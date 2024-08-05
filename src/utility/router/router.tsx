import { createBrowserRouter } from "react-router-dom";
import App from "../../App";
import { Login } from "../../Auth/Login";
import { RequireAuth } from "../../Auth/RequireAuth";
import { User } from "../../User/User";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <App />
  },
  {
    path: "/login",
    element: <Login />
  },
  {
    path: "/user",
    element: (
      <RequireAuth>
        <User />
      </RequireAuth>
    )
  }
]);
