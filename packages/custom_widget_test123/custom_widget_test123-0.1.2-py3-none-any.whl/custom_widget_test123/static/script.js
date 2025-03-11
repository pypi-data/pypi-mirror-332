// code from https://anywidget.dev/en/getting-started/

function render({ model, el }) {
    let button = document.createElement("button");
    button.innerHTML = `count is ${model.get("value")}`;
    button.addEventListener("click", () => {
      model.set("value", model.get("value") + 20);
      model.save_changes();
    });
    model.on("change:value", () => {
      button.innerHTML = `count is ${model.get("value")}`;
    });
    el.classList.add("counter-widget");
    el.appendChild(button);
  }
  export default { render };