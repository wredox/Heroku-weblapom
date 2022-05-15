function setCookie(c_name, value, exdays) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value = escape(value) + ((exdays == null) ? "" : ";samesite=lax;expires=" + exdate.toUTCString());
    document.cookie = c_name + "=" + c_value + ";path=/kereses";
}
function getCookie(c_name) {
    var i, x, y, ARRcookies = document.cookie.split(";");
    for (i = 0; i < ARRcookies.length; i++) {
        x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
        y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
        x = x.replace(/^\s+|\s+$/g, "");
        if (x == c_name) {
            return unescape(y);
        }
    }
}
function deleteCookie(cname) {
    var d = new Date(); //Create an date object
    d.setTime(d.getTime() - (1000*60*60*24)); //Set the time to the past. 1000 milliseonds = 1 second
    var expires = "expires=" + d.toGMTString(); //Compose the expirartion date
    window.document.cookie = cname+"="+"; "+expires;//Set the cookie with name and the expiration date

}
function county_change() {
    var county_change = $('#county')[0].value;
    setCookie("search_county", county_change, 1);
}
function species_change() {
    var species_change = $('#species')[0].value;
    setCookie("search_species", species_change, 1);
}
function age_change() {
    var age_change = $('#age')[0].value;
    setCookie("search_age", age_change, 1);
}

function size_change() {
    var size_change = $('#size')[0].value;
    setCookie("search_size", size_change, 1);
}
function hair_change() {
    var hair_change = $('#hair')[0].value;
    setCookie("search_hair", hair_change, 1);

}
function set_spayed() {
    var spayed_check = document.getElementById("spayed");
    if (spayed_check.checked == true){
        setCookie("search_spayed", 1, 1);
    }
    if (spayed_check.checked == false){
        setCookie("search_spayed", 0, 1);
    }
}
function set_dog_ok() {
    var dog_ok = document.getElementById("dog_ok");
    if (dog_ok.checked == true){
        setCookie("search_dog_ok", 1, 1);
    }
    if (dog_ok.checked == false){
        setCookie("search_dog_ok", 0, 1);
    }
}
function set_cat_ok() {
    var cat_ok = document.getElementById("cat_ok");
    if (cat_ok.checked == true){
        setCookie("search_cat_ok", 1, 1);
    }
    if (cat_ok.checked == false){
        setCookie("search_cat_ok", 0, 1);
    }
}
function set_kids_ok() {
    var kids_ok = document.getElementById("kids_ok");
    if (kids_ok.checked == true){
        setCookie("search_kids_ok", 1, 1);
    }
    if (kids_ok.checked == false){
        setCookie("search_kids_ok", 0, 1);
    }
}

$(document).ready(function() {
    if (getCookie("search_county")){
        $('#county')[0].value = getCookie("search_county");
    }
    if (getCookie("search_species")){
    	$('#species')[0].value = getCookie("search_species");
    }
    if (getCookie("search_age")) {
        $('#age')[0].value = getCookie("search_age");
    }
    if (getCookie("search_size")){
        $('#size')[0].value = getCookie("search_size");
    }
	if (getCookie("search_hair")){
        $('#hair')[0].value = getCookie("search_hair");
    }
	if (getCookie("search_spayed") == 1){
	    document.getElementById("spayed").checked = true;
    } else { document.getElementById("spayed").checked = false; }
    if (getCookie("search_dog_ok") == 1){
	    document.getElementById("dog_ok").checked = true;
    } else { document.getElementById("dog_ok").checked = false; }
    if (getCookie("search_cat_ok") == 1){
	    document.getElementById("cat_ok").checked = true;
    } else { document.getElementById("cat_ok").checked = false; }
    if (getCookie("search_kids_ok") == 1){
	    document.getElementById("kids_ok").checked = true;
    } else { document.getElementById("kids_ok").checked = false; }

	document.saveSearch.county.value = getCookie("search_county");
	document.saveSearch.species.value = getCookie("search_species");
	document.saveSearch.age.value = getCookie("search_age");
	document.saveSearch.size.value = getCookie("search_size");
	document.saveSearch.hair.value = getCookie("search_hair");
	document.saveSearch.spayed.value = getCookie("search_spayed");
})

function openForm() {
    document.getElementById("sh_Popup").style.display="block";
}
function closeForm() {
    document.getElementById("sh_Popup").style.display= "none";
}
window.onclick = function(event) {
    var modal = document.getElementById('sh_Popup');
    if (event.target == modal) {
        closeForm();
    }
}

/* Ajax */
$(function(){
	$('saveSearch.button.saveButton').click(function(){
		var county = $('#county').val();
		var species = $('#species').val();
		$.ajax({
			url: '/saveSearch',
			data: $('saveSearch').serialize(),
			type: 'POST',
			success: function(response){
			    if (response == 'ok'){
                    $( "p.response" ).html( "A keresés elmentve!" );
                }
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});