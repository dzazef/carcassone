class BoardClass {

    print_something = (canvas) => {
        let ctx = canvas.getContext("2d");
        ctx.beginPath();
        ctx.arc(100, 75, 50, 0, 2 * Math.PI);
        ctx.stroke();
    }

}

export default BoardClass