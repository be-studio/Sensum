import { useUsersQuery } from "./hooks/useUsersQuery";

export const User = () => {
  const { data: users } = useUsersQuery();

  return <>User</>;
};
