import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";
import { User } from "./User";
import { QueryClientProvider, QueryClient } from "react-query";

const logoutSpy = vi.fn().mockResolvedValueOnce({}).mockRejectedValueOnce({})

describe("User Component", () => {
  vi.mock("./hooks/useUserQuery", () => {
    const actual = vi.importActual("./hooks/useUserQuery");
    return {
      ...actual,
      useUserQuery: () => ({
        data: []
      })
    }
  });
  vi.mock("react-router-dom", () => {
    const actual = vi.importActual("react-router-dom");
    return {
      ...actual,
      useNavigate: vi.fn()
    }
  });
  vi.mock("../Auth/hooks/useLogoutMutation", () => {
    const actual = vi.importActual("../Auth/hooks/useLogoutMutation");
    return {
      ...actual,
      useLogoutMutation: () => ({
        mutateAsync: logoutSpy
      })
    };
  });

  const queryClient = new QueryClient();

  it("should render", () => {
    render(
      <QueryClientProvider client={queryClient}><User /></QueryClientProvider>);

    expect(screen.getByRole("heading", { name: "User" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Logout" })).toBeInTheDocument();
  });

  it("should trigger logout mutation on clicking 'Logout' button", async() => {
    const user = userEvent.setup();

    render(
      <QueryClientProvider client={queryClient}><User /></QueryClientProvider>);

    await user.click(screen.getByRole("button", { name: "Logout" }));

    expect(logoutSpy).toHaveBeenCalled();
  });
});
