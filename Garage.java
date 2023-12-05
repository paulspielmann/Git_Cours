import java.util.ArrayList;
import java.util.Comparator;

class Vehicule {
    private float taxe = 0.05f; // 5% de taxe par defaut mais modifiable
    private int annee;
    private String marque;
    private String modele;
    private float prix;

    public Vehicule(String m, String mo, int a, float p) {
        modele = mo;
        marque = m;
        annee = a;
        prix = p;
    }

    public Vehicule(Vehicule v) {
        new Vehicule(v.marque, v.modele, v.annee, v.prix);
    }

    public String toString() {
        String res = marque + " " + modele + " d'annee " + annee + " de prix " + prix;
        return res;
    }

    public int getAnnee() { return annee; }
    public String getMarque() { return marque; }
    public String getModele() { return modele; }
    public float getPrix() { return prix; }
    public float getTaxe() { return taxe; }

    public float prixVente() {
        float res = prix + prix * taxe;
        return res;
    }

    // Comparaison en fonction du prix de vente
    /* public Vehicule compare(Vehicule v) {
        if (this.prixVente() < v.prixVente()) {
            return this;
        }
        else return v;
    } */
}

class VehiculeFrancais extends Vehicule {
    private final float taxeFrancaise = 0.01f;

    public VehiculeFrancais(String m, String mo, int a, float p) {
        super(m, mo, a, p);
    }

    public String toString() {
        return super.toString() + " -> Ce vehicule est Francais";
    }

    public float prixVente() {
        float res = (getPrix() + getPrix() * getTaxe());
        res += res * taxeFrancaise;
        return res;
    }
}

class VehiculeComparator implements Comparator<Vehicule> {
    @Override
    public int compare(Vehicule v1, Vehicule v2) {
        return Float.compare(v1.getPrix(), v2.getPrix());
    }
}

class Garage {
    private ArrayList<Vehicule> stock;

    public static void main(String[] args) {
        Garage garage = new Garage();
        garage.ajoutVehicule(new VehiculeFrancais("Peugeot", "306", 2008, 10500f));
        garage.ajoutVehicule(new Vehicule("Citroen", "C3", 2006, 15000f));
        garage.ajoutVehicule(new Vehicule("Peugeot", "206", 1990, 8500f));
        garage.ajoutVehicule(new Vehicule("Peugeot", "207", 2010, 12500f));
        garage.ajoutVehicule(new Vehicule("Tesla", "Modele M", 2018, 75000f));
        garage.ajoutVehicule(new Vehicule("Toyota", "Corolla", 2013, 32000f));

        System.out.println(" -------- !! GARAGE NON TRIE !! --------");
        garage.afficheGarage();
        System.out.println(" -------- !! GARAGE TRIE !! --------");
        garage.triParPrix();
        garage.afficheGarage();
    }

    public Garage() {
        stock = new ArrayList<Vehicule>();
    }

    // Init garage avec un vehicule
    public Garage(Vehicule v) {
        stock = new ArrayList<Vehicule>();
        stock.add(v);
    }

    public void afficheGarage() {
        for (Vehicule v : stock) {
            System.out.println(v.toString());
        }
    }

    public void ajoutVehicule(Vehicule v) { stock.add(v); }

    public void removeVehicule(Vehicule d) {
        for (Vehicule v : stock) {
            if (v == d) {

            }
        }    
    }

    public void triParPrix() {
        VehiculeComparator compar = new VehiculeComparator();
        stock.sort(compar);
        //stock.sort((v1, v2) -> (v1.getPrix() - v2.getPrix()));
    }
}