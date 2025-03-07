from unittest.mock import Mock, call

from kirin import ir
from bloqade import qasm2
from bloqade.noise import native
from bloqade.pyqrack import StackMemory, PyQrackInterpreter

simulation = qasm2.extended.add(native)


def run_mock(size, program: ir.Method, rng_state: Mock) -> Mock:
    memory = StackMemory(total=2, allocated=0, sim_reg=Mock())

    PyQrackInterpreter(program.dialects, memory=memory, rng_state=rng_state).run(
        program, ()
    ).expect()

    return memory.sim_reg


def test_pauli_channel():
    @simulation
    def test_atom_loss():
        q = qasm2.qreg(2)
        native.pauli_channel(
            [q[0]],
            px=0.1,
            py=0.4,
            pz=0.3,
        )
        native.pauli_channel(
            [q[1]],
            px=0.1,
            py=0.4,
            pz=0.3,
        )
        return q

    rng_state = Mock()
    rng_state.choice.side_effect = ["y", "i"]
    sim_reg = run_mock(2, test_atom_loss, rng_state)
    sim_reg.assert_has_calls([call.y(0)])


def test_cz_pauli_channel_false():
    @simulation
    def test_atom_loss():
        q = qasm2.qreg(2)
        native.atom_loss_channel([q[0]], prob=0.7)
        native.atom_loss_channel(
            qargs=[q[1]],
            prob=0.7,
        )
        native.cz_pauli_channel(
            [q[0]],
            [q[1]],
            px_ctrl=0.1,
            py_ctrl=0.4,
            pz_ctrl=0.3,
            px_qarg=0.2,
            py_qarg=0.2,
            pz_qarg=0.2,
            paired=False,
        )  # no noise here
        qasm2.cz(q[0], q[1])
        native.atom_loss_channel([q[0]], prob=0.4)
        native.atom_loss_channel([q[1]], prob=0.7)
        native.cz_pauli_channel(
            [q[0]],
            [q[1]],
            px_ctrl=0.1,
            py_ctrl=0.4,
            pz_ctrl=0.3,
            px_qarg=0.2,
            py_qarg=0.2,
            pz_qarg=0.2,
            paired=False,
        )
        qasm2.cz(q[0], q[1])
        return q

    rng_state = Mock()
    rng_state.choice.side_effect = ["y"]
    rng_state.uniform.return_value = 0.5
    sim_reg = run_mock(2, test_atom_loss, rng_state)
    sim_reg.assert_has_calls([call.mcz([0], 1), call.force_m(0, 0), call.y(1)])


def test_cz_pauli_channel_true():
    @simulation
    def test_atom_loss():
        q = qasm2.qreg(2)
        native.atom_loss_channel([q[0]], prob=0.7)
        native.atom_loss_channel([q[1]], prob=0.7)
        native.cz_pauli_channel(
            [q[0]],
            [q[1]],
            px_ctrl=0.1,
            py_ctrl=0.4,
            pz_ctrl=0.3,
            px_qarg=0.2,
            py_qarg=0.2,
            pz_qarg=0.2,
            paired=True,
        )  # no noise here
        qasm2.cz(q[0], q[1])
        native.atom_loss_channel([q[0]], prob=0.4)
        native.atom_loss_channel([q[1]], prob=0.7)
        native.cz_pauli_channel(
            [q[0]],
            [q[1]],
            px_ctrl=0.1,
            py_ctrl=0.4,
            pz_ctrl=0.3,
            px_qarg=0.2,
            py_qarg=0.2,
            pz_qarg=0.2,
            paired=True,
        )
        qasm2.cz(q[0], q[1])
        return q

    rng_state = Mock()
    rng_state.choice.side_effect = ["y", "x"]
    rng_state.uniform.return_value = 0.5
    sim_reg = run_mock(2, test_atom_loss, rng_state)

    sim_reg.assert_has_calls([call.y(0), call.x(1), call.mcz([0], 1)])


if __name__ == "__main__":
    test_pauli_channel()
    test_cz_pauli_channel_false()
    test_cz_pauli_channel_true()
