var connectionParams = {
  method: "GET",
  mode: "cors",
  headers: {
    "Access-Control-Allow-Origin": "*",
    Accept: "application/json",
    "Content-Type": "application/json",
  },
};

window.onload = (() => {
  var prodDiv = document.getElementById("product-details");
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const uniqueId = urlParams.get("uniqueId");
  fetch(`http://127.0.0.1:5000/product?uniqueId=${uniqueId}`, connectionParams)
    .then((response) => response.json())
    .then((data) => {
      const productMap = data;
      const title = productMap["title"];
      const image = productMap["image"];
      const price = productMap["price"];
      const description = productMap["description"];
      document.getElementById("prod-title").innerHTML = title;
      document.getElementById("prod-name").innerHTML = title;
      prodDiv.innerHTML += `
          <div class="image-slider">
            <img id="prod-img" src="${image}" class="product-border"/>
          </div>
          <div class="details">
            <p class="product-title">
              ${title}
            </p>
            <span class="product-price">$${price}</span>
            <br>
            <br>
            <h4>Product Description</h4>
            <p class="product-des">
              ${description}
            </p>
          </div>`;
    });
})();
