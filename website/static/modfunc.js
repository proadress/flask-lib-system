export async function post(url, data) {
  try {
    const response = await fetch(url, {
      method: "POST",
      body: data,
    });
    const req = await response.json();
    return req;
  } catch (error) {
    console.log("post_error", error);
    return "post_error";
  }
}

export async function get(url) {
  try {
    const response = await fetch(url, {
      method: "GET",
    });
    const req = await response.json();
    return req;
  } catch (error) {
    console.log("post_error", error);
    return "post_error";
  }
}

export function create_flash(message) {
  const flash = document.createElement("div");
  flash.classList.add(
    "alert",
    "alert-danger",
    "alert-dismissible",
    "fade",
    "show"
  );
  flash.setAttribute("role", "alert");
  flash.innerHTML = `
          ${message}
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      `;
  const errorContainer = document.getElementById("error");
  errorContainer.innerHTML = "";
  errorContainer.appendChild(flash);
}
