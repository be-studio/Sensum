const getCookie = (key: string) => {
  const value = document.cookie.match("(^|;)\\s*" + key + "\\s*=\\s*([^;]+)");
  return value ? value.pop() : "";
};

export default getCookie;
