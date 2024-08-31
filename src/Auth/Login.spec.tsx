import { render, screen } from "@testing-library/react";
import { vi } from "vitest";
import { Login } from "./Login";
import { QueryClientProvider, QueryClient } from "react-query";

describe("Login Component", () => {
  vi.mock("react-router-dom", () => {
    const actual = vi.importActual("react-router-dom");
    return {
      ...actual,
      useNavigate: vi.fn()
    }
  });

  const queryClient = new QueryClient();

  it("should render", () => {
    render(
      <QueryClientProvider client={queryClient}>
        <Login />
      </QueryClientProvider>
    );

    expect(screen.getByRole("textbox", { name: "email" })).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Login" })).toBeInTheDocument();
  });
});
