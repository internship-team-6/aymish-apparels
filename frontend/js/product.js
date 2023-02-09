const productFunction = function () {
  let q = localStorage.getItem("query");
  var prod_div = document.getElementById("product-details");
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const uniqueId = urlParams.get("uniqueId");
  if (uniqueId === null) {
    return;
  }
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
      const title = productDict["title"];
      const image = productDict["image"];
      const price = productDict["price"];
      const description = productDict["description"];
      let prod_title = document.getElementById("prod-title")
      prod_title.innerHTML = `${title}`
      let prod_name = document.getElementById("prod-name")
      prod_name.innerHTML = `${title}`
      
      prod_div.innerHTML += `
          <div class="image-slider">
            <img id="product_image" src="${image}" class="product-border"/>
          </div>
          <div class="details">
            <p class="product-title">
              ${title}
            </p>
            <span class="product-price">$${price}</span>
            <p class="product-des">
              ${description}
            </p>
          </div>`;
      // window.location = "404.html";
      // document.getElementById("loader").style.display = "none";
    })
    .catch((err) => {
      console.log(err);
    });
};

onload = productFunction();
