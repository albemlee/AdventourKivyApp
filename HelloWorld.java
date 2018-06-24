import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

public class HelloWorld {

    public static void main(String[] args) {
        // Prints "Hello, World" to the terminal window.
        Dataset<Row> df = spark.read().json("base_wiki_data.json");
        df.show();
    }

}
