// ✅ Vérification que le fichier est bien chargé
document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ Fichier custom.js chargé avec succès !");
    
    // ✅ Animation sur les boutons au survol
    document.querySelectorAll(".btn").forEach(btn => {
        btn.addEventListener("mouseover", () => {
            btn.style.opacity = "0.8";
        });
        btn.addEventListener("mouseout", () => {
            btn.style.opacity = "1";
        });
    });

    // ✅ Confirmation avant suppression d'un patient
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function (event) {
            const confirmDelete = confirm("⚠️ Voulez-vous vraiment supprimer ce patient ?");
            if (!confirmDelete) {
                event.preventDefault(); // Empêche l'action si l'utilisateur annule
            }
        });
    });
});
