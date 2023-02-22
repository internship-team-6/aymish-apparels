// parameters to connect while using the fetch promise on any given url
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

  // get values for parameters
  const urlParams = new URLSearchParams(queryString);
  const uniqueId = urlParams.get("uniqueId");

  // get product details for given id
  fetch(`http://127.0.0.1:5000/product?uniqueId=${uniqueId}`, connectionParams)
    .then((response) => response.json())
    .then((data) => {
      const productMap = data;
      const title = productMap["title"];
      const image = productMap["image"];
      const price = productMap["price"];
      const description = productMap["description"];
      
      // update page with product details
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

      // get recommendations for selected product
      fetch(
        `http://127.0.0.1:5000/recommendations?uniqueId=${uniqueId}`,
        connectionParams
      )
        .then((response) => response.json())
        .then((data) => {
          const pages = data["pages"];
          
          // update page with recommendations
          let prodListDiv = document.getElementById("product-list-div");
          const newInnerHTML = data
            .map(
              (product) => `
                  <div class="product-recommend" id="product-list-div" onclick = "window.open('product.html?uniqueId=${product["id"]}','_blank');">
                    <div class="product-card">
                      <div class="product-image">
                        <img src="${product["image"]}" class="product-thumb product-border" alt="" />
                      </div>
                      <div class="product-info">
                        <p class="product-title">${product["name"]}</p>
                        <span class="price">$${product["price"]}</span>
                      </div>
                    </div>
                  </div>
                  `
            )
            .reduce((x, y) => x + y);
          prodListDiv.innerHTML += newInnerHTML;
        })
        .catch((err) => {
          window.location.href = "./404.html?";
        });
    })
    .catch((err) => {
      window.location.href = "./404.html?";
    });
})();
