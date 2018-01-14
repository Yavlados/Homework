$(function () {
    $('#id_subject').change(function () {
        if ($("option:selected", this).text() === "Не выбрано")
        {
            $('#id_tutor').attr("disabled", true).prop('selectedIndex',0);
        }
        else
        {
            $('#id_tutor').attr("disabled", false);
            var url = "/db/tutors/" + $(this).val() + "/related_json_tutors";
            $.getJSON(url, function(tutors) {
                var options = '<option value="" selected>Не выбрано</option>';
                for (var i = 0; i < tutors.length; i++) {
                    options += '<option value="' + tutors[i].pk + '">' + tutors[i].fields['surname'] + " " +
                        tutors[i].fields['name'] + " " + tutors[i].fields['patronymic'] + '</option>';
                }
                $("#id_tutor").html(options);
            });
        }
    });


    var objects_per_page = parseInt($('#per-page').text());
    var count_current_objects = parseInt($('#per-page').text());
    var courses = [];
    $.getJSON("/db/courses/all_json_courses", function (data) {
        $.each(data, function (i, course) {
            courses.push(course);
        })
    });
    $('.pagination').hide();
    $(document).scroll(function () {
        var curScroll = $(this).scrollTop();
        var maxScroll = document.body.scrollHeight - $(window).height();
        if (curScroll === maxScroll)
        {
            if (count_current_objects < courses.length-1)
            {
                for (var i = count_current_objects; i < objects_per_page+count_current_objects; i++)
                {
                    if (courses[i].fields.photo)
                    {
                        $('.course').append("<a href=\"/courses/" + courses[i].pk + "\" class=\"course-element\">" +
                            "<div class=\"course-photo\">" +
                            "<img class=\"img-course\" src=\"/media/" + courses[i].fields.photo +
                            "\" width=\"100%\" height=\"100%\">" +
                            "</div><span class=\"course-name\">" + courses[i].fields.name_course + "</span>\n" +
                            "                                <span class=\"course-tutor\">" + courses[i].fields.tutor +
                            "</span></a>");
                    }
                    else
                    {
                        $('.course').append("<a href=\"/courses/" + courses[i].pk + "\" class=\"course-element\">" +
                            "<div class=\"course-photo\"></div>" +
                            "<span class=\"course-name\">" + courses[i].fields.name_course + "</span>\n" +
                            "                                <span class=\"course-tutor\">" + courses[i].fields.tutor +
                            "</span></a>");
                    }
                    if (i === courses.length-1)
                    {
                        break;
                    }
                }
                $(this).scrollTop(document.body.scrollHeight - $(window).height() - 900);
                count_current_objects = i;
            }
        }
    });


    $('#id_feedback_info, #id_tovar').on("invalid", function (e) {
        e.preventDefault();
    });
    $('#id_feedback_info').click(function () {
        $('#error_id_feedback_info').fadeOut(2000);
    });
    $('#id_tovar').click(function () {
        $('#error_id_tovar').fadeOut(2000);
    });



    $('#btn_add').click(function (e) {
        if ($("option:selected", '#id_tovar').text() === "Не выбрано")
        {
            e.preventDefault();
            $('#error_id_tovar').fadeIn(1000);
        }
        else if ($('#id_feedback_info').val() === "Вы ничего не написали :(")
        {
             e.preventDefault();
            $('#error_id_feedback_info').fadeIn(1000)
        }
    });


    $('#Entry').click(function (e) {
        e.preventDefault();
        var tovar_show_url = "/tovar_show" + $('#id_tovar').text();
        $.ajax({
            type: "POST",
            url: tovar_show_url,
            data: {csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
            success:function () {
                $('').append($('#tovar_show').text());
                $('#Entry').css({"background-color": "gray", "box-shadow": "none"}).text("Вы уже записаны!").prop(
                    "disabled", true);
            }
        })
    })
});
