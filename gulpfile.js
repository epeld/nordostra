
var gulp = require('gulp');
var jade = require('gulp-jade');
var stylus = require('gulp-stylus');

gulp.task('html', function() {
    return gulp.src('jade/*.jade')
                .pipe(jade())
                .pipe(gulp.dest('build/html'));
});

gulp.task('styles', function() {
    return gulp.src('stylus/*.styl')
        .pipe(stylus())
        .pipe(gulp.dest('build/styles'));
});

gulp.task('images', function() {
    return gulp.src('images/*').pipe(gulp.dest("build/images"));
});

gulp.task('default', ['styles', 'html', 'images']);
