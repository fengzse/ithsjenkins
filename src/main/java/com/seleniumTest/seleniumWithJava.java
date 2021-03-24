package com.seleniumTest;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.concurrent.TimeUnit;

public class seleniumWithJava {
    WebDriver driver;
    WebDriverWait wait;
    seleniumWithJava(WebDriver dr){
        driver=dr;
    }

    public String seleniumRun(String url, String search, String item){
        driver.get(url);
        wait = new WebDriverWait(driver,5);
        wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//input[@id='twotabsearchtextbox']")));
        driver.findElement(By.xpath("//input[@id='twotabsearchtextbox']")).sendKeys(search);
        driver.findElement(By.xpath("//*[@id='nav-search-submit-button']")).click();

        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

        driver.findElement(By.partialLinkText(item)).click();
        return driver.getTitle();
    }

    public void tearDown(){
        driver.quit();
    }
}
