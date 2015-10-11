var gulp = require("gulp");

var rename     = require("gulp-rename")
    concat     = require("gulp-concat")
    sass       = require("gulp-sass");

var scss_dir = "_styles";
var css_dist = "css";


gulp.task("default", ["watch"]);
gulp.task("watch", function() {
    gulp.watch(scss_dir + "/**/*.scss", ["build-css"]);
});

gulp.task("clean", function() {
    del([css_dist]);
});

gulp.task("build-css", function() {
    return gulp.src(scss_dir + "/**/*.scss")
        .pipe(sass({outputStyle: "compressed"})
            .on("error", sass.logError))
        .pipe(concat("style.css"))
        .pipe(gulp.dest(css_dist));
});
