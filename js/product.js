window.onload = function () {
  let q = localStorage.getItem("query");
  var prod_div = document.getElementById("product-details");
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const uniqueId = urlParams.get("uniqueId");
  if (uniqueId === null) {
    return;
  }
  console.log(uniqueId)
  fetch(`http://127.0.0.1:5000/product?uniqueId=${uniqueId}`, {
    method: "GET",
    mode: "cors",
    headers: {
      "Access-Control-Allow-Origin": "*",
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const productDict = data;
      console.log(productDict);
      // const uniqueId = String(productDict["id"]);
      const title = productDict["title"];
      const image = productDict["image"];
      const price = productDict["price"];
      const description = productDict["description"];
      prod_div.innerHTML += `<section id="product-details">
          <div class="image-slider">
          <img id="product_image" src="${image}" />
          </div>
          <div class="details">
            <p class="product-title">
              ${title}
            </p>
            <span class="product-price">$${price}</span>
            <p class="product-des">
              ${description}
            </p>
          </div>
        </section>`;
      // window.location = "404.html";
      // document.getElementById("loader").style.display = "none";
    })
    .catch((err) => console.log(err));
};
