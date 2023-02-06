const searchProductListFunction = function () {
  const queryString = location.search;
  const urlParams = new URLSearchParams(queryString);
  q = urlParams.get("q");
  q = q == "" ? "*" : q;
  document.getElementById("product-query").innerHTML = q == "*" ? "all" : q;
  fetch("http://localhost:5000/search?" + new URLSearchParams({ q: q }), {
    method: "GET",
    mode: "cors",
    headers: {
      "Access-Control-Allow-Origin": "*",
      Accept: "application/json",
      "Content-Type": "application/json;charset=utf-8",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const products_arr = data;
      console.log(products_arr)
      let prod_list_div = document.getElementById("product-list-div");
      for (let i = 0; i < products_arr.length; i++) {
        let title = products_arr[i]["title"];
        let image = products_arr[i]["image"];
        let price = products_arr[i]["price"];
        let id = products_arr[i]["id"];
        prod_list_div.innerHTML += `
          <div class="product-container" id="product-list-div" onclick = "window.open('Product.html?uniqueId=${id}','_blank');">
            <div class="product-card">
              <div class="product-image">
                <img src="${image}" class="product-thumb" alt="" />
              </div>
              <div class="product-info">
                <p class="product-title">${title}</p>
                <span class="price">$${price}</span>
              </div>
            </div>
          </div>
        `;
      }
    });
};

onload = searchProductListFunction();
