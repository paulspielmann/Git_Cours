import java.util.ArrayList;
import java.util.Random;


class Tableau {
    
    public static void main(String[] args) {
        Tableau test = new Tableau(20);
        test.populate();
        System.out.println("------ !! TABLEAU NON TRIE !! ------");
        test.affiche();
        System.out.println("\n Moyenne de tab : " + test.moyenne());
        System.out.println("Frequence max : " + test.frequenceMax());
        System.out.println("------ !! TABLEAU TRIE !! ------");
        test.sort();
        test.affiche();
    }

    public ArrayList<Entier> tab;
    public int size;

    // Constructeur par defaut initialize la taille a 10
    public Tableau() {
        tab = new ArrayList<Entier>();
        size = 0;
    }

    public Tableau(int n) {
        tab = new ArrayList<Entier>(n);
        size = n;
    }

    public void populate() {
        Random rd = new Random();
        for (int i = 0; i < size; i++) {
            tab.add(i, new Entier(rd.nextInt(100)));
        }
    }

    public void affiche() {
        for (int i = 0; i < tab.size(); i++) {
            System.out.print(tab.get(i).val + " ");
        }
        System.out.print("\n");
    }

    public int moyenne() {

        if (tab.size() == 0) {
            System.out.println("Le tableau est vide");
            return 0;
        }

        int res = 0;
        int count = 0;

        for (Entier e : tab) {
            res += e.val;
            count++;
        }

        return (res / count);
    }

    public int getFirstIndexFromValue(int n) {
        if (size == 0) {
            System.out.println("Le tableau est vide");
            return -1;            
        }

        for (int i = 0; i < size; i++) {
            if (tab.get(i).val == n) {
                return i;
            }
        }

        return 0;
    }

    public int frequenceMax() {
        int mostCommon;
        int mostCommonFrequency = 0;
        
        if (size == 0) {
            System.out.println("Lee tableau est vide");
            return -1;
        }

        // On peut faire ca car on verifie que le tableau n'est pas vide
        mostCommon = tab.get(0).val;
        for (int i = 0; i < tab.size(); i++) {
            int currentFrequency = 1;

            for (int j = i + 1; j < tab.size(); j++) {
                if (tab.get(i).val == tab.get(j).val) {
                    currentFrequency++;
                }
            }

            if (currentFrequency > mostCommonFrequency) {
                mostCommonFrequency = currentFrequency;
                mostCommon = i;
            }
        }
        return mostCommon;
    }

    public boolean sorted() {
        for (int i = 0; i < size - 1; i++) {
            if (tab.get(i).val > tab.get(i + 1).val) {
                return false;
            }
        }
        return true;
    }

    public void sort() {
        int i = 1;
        int j;
        Entier x;

        while (i < size) {
            x = tab.get(i);
            j = i - 1;
            while (j >= 0 && tab.get(j).val > x.val) {
                tab.set(j + 1, tab.get(j));
                j--;
            }
            tab.set(j + 1, x);
            i++;
        }
    }
}

class Entier {
    public int val;

    public Entier(int n) {
        val = n;
    }
}