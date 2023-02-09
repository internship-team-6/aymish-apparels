const categoryProductListFunction = function () {
  const queryString = location.search;
  const urlParams = new URLSearchParams(queryString);
  const limit = 15;
  const page = parseInt(urlParams.get("page"));
  const offset = (page - 1) * limit;
  const catlevel1Id = urlParams.get("catlevel1Id");
  const catlevel2Name = urlParams.get("catlevel2Name");
  const sort = urlParams.get("sort");
  document.getElementById(
    "path"
  ).innerHTML += `<a href="./index.html" style="text-decoration:none;color:#bf616a" margin-left=20px>Home</a>/${catlevel1Id}/${
    catlevel2Name[0].toUpperCase() + catlevel2Name.slice(1)
  }`;
  let catlevel1Name = catlevel1Id == 1 ? "Men" : "Women";
  document.getElementById("product-query").innerHTML =
    catlevel1Name + " / " + catlevel2Name;
  document.getElementById(
    "cat-title"
  ).innerHTML = `${catlevel1Name}'s ${catlevel2Name}`;
  const catSearchParams = new URLSearchParams({
    catlevel1Id: catlevel1Id,
    catlevel2Name: catlevel2Name,
    sort: sort,
  });
  fetch("http://localhost:5000/category-product-list?" + catSearchParams, {
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
      let prod_list_div = document.getElementById("product-list-div");
      for (
        let counter = offset;
        counter < Math.min(offset + limit, products_arr.length);
        counter++
      ) {
        let title = products_arr[counter]["title"];
        let img = products_arr[counter]["image"];
        let price = products_arr[counter]["price"];
        let id = products_arr[counter]["id"];
        prod_list_div.innerHTML += `
          <div class="product-container" id="product-list-div" onclick = "window.open('product.html?uniqueId=${id}','_blank');">
            <div class="product-card">
              <div class="product-image">
                <img src="${img}" class="product-thumb product-border" alt="" />
              </div>
              <div class="product-info">
                <p class="product-title">${title}</p>
                <p class="price">$${price}</p>
              </div>
            </div>
          </div>
    `;
      }
      const pages =
        Math.floor(products_arr.length / limit) +
        (products_arr.length % limit && 1);
      let paginationId = document.getElementById("pagination");
      if (page !== 1) {
        let pageSearchParams = new URLSearchParams({ page: page - 1 });
        paginationId.innerHTML += `<a href="./category-product-list.html?${catSearchParams}&${pageSearchParams}">&lt</a>&nbsp`;
      }
      for (let temp_page = 1; temp_page <= pages; temp_page++) {
        let pageSearchParams = new URLSearchParams({ page: temp_page });
        if (temp_page === page) {
          console.log(temp_page);
          paginationId.innerHTML += `<a class = "active" href="./category-product-list.html?${catSearchParams}&${pageSearchParams}">${temp_page}</a>`;
        } else {
          paginationId.innerHTML += `<a href="./category-product-list.html?${catSearchParams}&${pageSearchParams}">${temp_page}</a>`;
        }
      }
      if (page !== pages) {
        let pageSearchParams = new URLSearchParams({ page: page + 1 });
        paginationId.innerHTML += `<a href="./category-product-list.html?${catSearchParams}&${pageSearchParams}">&gt</a>&nbsp`;
      }
    });
};

window.onload = categoryProductListFunction();
