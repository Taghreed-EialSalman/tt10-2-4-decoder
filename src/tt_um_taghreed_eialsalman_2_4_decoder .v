`default_nettype none
module tt_um_taghreed_eialsalman_2_4_decoder (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    // Internal wires for decoder inputs and outputs
    wire A = ui_in[0];
    wire B = ui_in[1];
    wire E = ui_in[2];
    wire [3:0] D;

    assign D[0] = ~(~A & ~B & ~E);
    assign D[1] = ~(~A &  B & ~E);
    assign D[2] = ~( A & ~B & ~E);
    assign D[3] = ~( A &  B & ~E);

    // Assign outputs
    assign uo_out[0] = D[0];
    assign uo_out[1] = D[1];
    assign uo_out[2] = D[2]; 
    assign uo_out[3] = D[3]; 
    assign uo_out[4] = 1'b0; 
    assign uo_out[5] = 1'b0; 
    assign uo_out[6] = 1'b0; 
    assign uo_out[7] = 1'b0;

    // All output pins must be assigned. If not used, assign to 0.
    assign uio_out = 0;
    assign uio_oe  = 0;

    // List all unused inputs to prevent warnings
    wire _unused = &{ena, clk, rst_n, ui_in[7:3], uio_in, 1'b0};

endmodule

