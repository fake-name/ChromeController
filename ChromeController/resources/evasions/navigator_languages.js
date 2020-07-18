{
  Object.defineProperty(navigator, "languages", {
    get: () => ["en-US", "en"], // TODO: Make configurable by user
  });
}