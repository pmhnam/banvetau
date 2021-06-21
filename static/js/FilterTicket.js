const div_tickets = document.querySelector('.tickets')
const input_time = document.querySelector('#time')
const input_route = document.querySelector('#route')
const input_date = document.querySelector('#date')
const list_ticket = []
var find_tickets = []
let ngayhomnay = new Date()
input_date.value = ngayhomnay.toISOString().split('T')[0]

defaultLoad();
// load_ticket()
function defaultLoad() {
    find_tickets = []
    thoigian = input_time.value
    tuyen = input_route.value
    ngaydi = input_date.value
    for (i of list_ticket) {
        if (thoigian == i.start_time) {
            if (tuyen == i.route) {
                if (ngaydi == i.start_day) {
                    find_tickets.push(i)
                }
            }
        }
    }
    display_tickets(find_tickets);
}
input_time.addEventListener('input', (e) => {
    find_tickets = []
    thoigian = e.target.value
    tuyen = input_route.value
    ngaydi = input_date.value
    for (i of list_ticket) {
        if (thoigian == i.start_time) {
            if (tuyen == i.route) {
                if (ngaydi == i.start_day) {
                    find_tickets.push(i)
                }
            }
        }
    }
    display_tickets(find_tickets);
})

input_date.addEventListener('input', (e) => {
    find_tickets = []
    thoigian = input_time.value
    tuyen = input_route.value
    ngaydi = e.target.value
    for (i of list_ticket) {
        if (thoigian == i.start_time) {
            if (tuyen == i.route) {
                if (ngaydi == i.start_day) {
                    find_tickets.push(i)
                }
            }
        }
    }
    display_tickets(find_tickets);
})

input_route.addEventListener('input', (e) => {
    find_tickets = []
    thoigian = input_time.value
    tuyen = e.target.value
    ngaydi = input_date.value
    for (i of list_ticket) {
        if (thoigian == i.start_time) {
            if (tuyen == i.route) {
                if (ngaydi == i.start_day) {
                    find_tickets.push(i)
                }
            }
        }
    }
    display_tickets(find_tickets);
})


function chuyendoithang(key) {
    let result = ''
    switch (key) {
        case "Jan.":
            result = '01'
            break;
        case "Feb.":
            result = '02'
            break;
        case "March":
            result = '03'
            break;
        case "April":
            result = '04'
            break;
        case "May":
            result = '05'
            break;
        case "June":
            result = '06'
            break;
        case "July":
            result = '07'
            break;
        case "Aug.":
            result = '08'
            break;
        case "Sept.":
            result = '09'
            break;
        case "Oct.":
            result = '10'
            break;
        case "Nov.":
            result = '11'
            break;
        case "Dec.":
            result = '12'
            break;
    }
    return result
}

function display_tickets(find_tickets) {
    div_tickets.innerHTML = ''
    for (i of find_tickets) {
        let div = document.createElement('div')
        let input_choice = document.createElement('input')
        let label_choice = document.createElement('label')
        let span_seat = document.createElement('span')
        let span_cost = document.createElement('span')
        let span_type = document.createElement('span')

        //add className
        span_seat.classList.add("seat_slot");
        input_choice.classList.add("choose_seat");
        div.classList.add("seat_contain");

        div.appendChild(input_choice)
        div.appendChild(label_choice)
        label_choice.appendChild(span_seat)
        label_choice.appendChild(span_cost)
        label_choice.appendChild(span_type)

        input_choice.setAttribute('type', "checkbox")
        input_choice.setAttribute('name', i.id)
        input_choice.setAttribute('value', i.id)
        if (i.status == 'T') {
            input_choice.setAttribute('onclick', "return false;")
            input_choice.classList.add('active')
        }

        span_seat.textContent = i.seat
        // span_cost.textContent = ', giá: ' + i.cost
        // span_type.textContent = ', loại: ' + i.type

        div_tickets.appendChild(div)
    }
    choosing_seat();
}


function choosing_seat() {
    const clickSlot = document.querySelectorAll(".seat_slot");
    const btnChooseSeat = document.querySelectorAll(".choose_seat");
    const slotContain = document.querySelectorAll(".seat_contain");
    slotContain.forEach(btnChoosing => {
        btnChoosing.addEventListener("click", () => {
            btnChoosing.classList.toggle("choosing");
            // console.log(btnChoosing);
        })
    })

}