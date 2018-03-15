package com.example.hello;

import com.blade.embedd.EmbedJettyServer;
import com.blade.mvc.view.ViewSettings;
import com.blade.mvc.view.template.VelocityTemplateEngine;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.ArrayList;
import java.util.List;

import static com.blade.Blade.$;

/**
 * Hello Blade!
 */
public class Application {

    private static final Logger LOGGER = LoggerFactory.getLogger(Application.class);

    public static void main(String[] args) throws Exception {

        ViewSettings.$().templateEngine(new VelocityTemplateEngine());

        $().get("/", (request, response) -> response.html("<h1>Hello Blade！</h1>")).get("/hello", (request, response) -> {
            request.attribute("name", "jack");
            response.render("hello.vm");
        }).get("/users", (request, response) -> {
            List<User> users = new ArrayList<>(2);
            users.add(new User("jack", 22));
            users.add(new User("王爵nice", 24));
            response.json(users);
        }).before("/.*", (request, response) -> LOGGER.info("before ...")).start(EmbedJettyServer.class);

    }

}