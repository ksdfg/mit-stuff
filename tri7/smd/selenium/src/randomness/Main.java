package randomness;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import static java.lang.Thread.sleep;

public class Main {

    public static void main (String[] args) throws InterruptedException {
        System.setProperty("webdriver.gecko.driver", "K:\\script-stuff\\script-bot\\whatsapp_stuff\\geckodriver.exe");
        WebDriver driver = new FirefoxDriver();

        driver.get("https://www.gmail.com");

        driver.findElement(By.id("identifierId")).sendKeys("ksdfg123\n");
        (new WebDriverWait(driver, 3)).until(ExpectedConditions.elementToBeClickable(By.name("password")));
        driver.findElement(By.name("password")).sendKeys("wrongpassword\n");
        sleep(10000);

        driver.close();
    }

}