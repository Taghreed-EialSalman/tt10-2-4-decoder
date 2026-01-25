import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start 2-to-4 Decoder Test")

    # Create a clock (required by Tiny Tapeout template)
    clock = Clock(dut.clk, 10, units="us")  # 100 kHz
    cocotb.start_soon(clock.start())

    # Reset sequence (template requirement)
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Starting functional verification")

    # Test vectors: (E, A, B, D0, D1, D2, D3)
    # Matches the truth table used in your report
    test_vectors = [
        (0, 0, 0, 0, 1, 1, 1),
        (1, 0, 0, 1, 1, 1, 1),
        (0, 0, 1, 1, 0, 1, 1),
        (1, 0, 1, 1, 1, 1, 1),
        (0, 1, 0, 1, 1, 0, 1),
        (1, 1, 0, 1, 1, 1, 1),
        (0, 1, 1, 1, 1, 1, 0),
        (1, 1, 1, 1, 1, 1, 1),
    ]

    # Apply all test cases
    for (E, A, B, expD0, expD1, expD2, expD3) in test_vectors:
        dut.ui_in[0].value = A
        dut.ui_in[1].value = B
        dut.ui_in[2].value = E

        # Allow time for outputs to settle
        await ClockCycles(dut.clk, 25)

        # Assertions
        assert int(dut.uo_out[0].value) == expD0, f"Fail: E={E} A={A} B={B} D0"
        assert int(dut.uo_out[1].value) == expD1, f"Fail: E={E} A={A} B={B} D1"
        assert int(dut.uo_out[2].value) == expD2, f"Fail: E={E} A={A} B={B} D2"
        assert int(dut.uo_out[3].value) == expD3, f"Fail: E={E} A={A} B={B} D3"

        dut._log.info(
            f"PASS: E={E} A={A} B={B} | "
            f"D={expD3}{expD2}{expD1}{expD0}"
        )

    dut._log.info("All 2-to-4 decoder test cases PASSED ✅")
