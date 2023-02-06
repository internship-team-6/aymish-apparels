const categoryProductListFunction = function () {
  const queryString = location.search;
  const urlParams = new URLSearchParams(queryString);
  catlevel1Id = urlParams.get("catlevel1Id");
  catlevel2Name = urlParams.get("catlevel2Name");
  document.getElementById("product-query").innerHTML = catlevel2Name;
  fetch(
    "http://localhost:5000/category-product-list?" +
      new URLSearchParams({
        catlevel1Id: catlevel1Id,
        catlevel2Name: catlevel2Name,
      }),
    {
      method: "GET",
      mode: "cors",
      headers: {
        "Access-Control-Allow-Origin": "*",
        Accept: "application/json",
        "Content-Type": "application/json;charset=utf-8",
      },
    }
  )
    .then((response) => response.json())
    .then((data) => {
      const products_arr = data;
      let prod_list_div = document.getElementById("product-list-div");
      for (let i = 0; i < products_arr.length; i++) {
        let title = products_arr[i]["title"];
        let img = products_arr[i]["image"];
        let price = products_arr[i]["price"];
        let id = products_arr[i]["id"];
        prod_list_div.innerHTML += `
          <div class="product-container" id="product-list-div" onclick = "window.open('product.html?uniqueId=${id}','_blank');">
            <div class="product-card">
              <div class="product-image">
                <img src="${img}" class="product-thumb" alt="" />
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

onload = categoryProductListFunction();
