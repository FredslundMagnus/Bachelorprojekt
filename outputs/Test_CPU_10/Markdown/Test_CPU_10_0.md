/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Test_CPU_10-0
    Main :                      teleport
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     0.1
    Batch :                     25
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1 minutes.
    Hours used :                0 hours.

# Profiling


      13610756 function calls (13491620 primitive calls) in 60.19 seconds

##    Ordered by: cumulative time
   List reduced from 387 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   60.194   60.194 {built-in method builtins.exec}
                      1    0.020    0.020   60.194   60.194 <string>:1(<module>)
                      1    0.126    0.126   60.174   60.174 main.py:46(teleport)
                   4458    0.032    0.000   46.984    0.011 agent.py:29(learn)
                   4458    0.386    0.000   37.605    0.008 learner.py:42(Qlearn)
                   2229    0.354    0.000   34.540    0.015 agent.py:54(_learn)
           133498/15070    0.815    0.000   24.087    0.002 module.py:715(_call_impl)
                  10612    0.039    0.000   23.559    0.002 network.py:28(forward)
                  10612    0.207    0.000   23.419    0.002 container.py:115(forward)
                  21224    0.073    0.000   18.014    0.001 conv.py:422(forward)
                  21224    0.089    0.000   17.914    0.001 conv.py:414(_conv_forward)
                  21224   17.815    0.001   17.815    0.001 {built-in method conv2d}
                   4458    0.042    0.000   17.219    0.004 tensor.py:181(backward)
                   4458    0.036    0.000   17.177    0.004 __init__.py:68(backward)
                   4458   17.032    0.004   17.032    0.004 {method 'run_backward' of 'torch._C._EngineBase' objects}
                   2229    0.184    0.000   12.402    0.006 agent.py:117(_learn)
                   3925    0.120    0.000   10.764    0.003 agent.py:49(__call__)
                   4458    0.062    0.000    6.716    0.002 grad_mode.py:23(decorate_context)
                   4458    0.230    0.000    6.545    0.001 adam.py:55(step)
                   4458    1.142    0.000    5.431    0.001 functional.py:53(adam)
                   2229    0.013    0.000    3.771    0.002 game.py:42(step)
                   2229    0.018    0.000    3.612    0.002 layers.py:827(step)
                   2229    0.048    0.000    3.377    0.002 agent.py:112(__call__)
                  27378    0.096    0.000    2.675    0.000 linear.py:92(forward)
                  27378    0.166    0.000    2.534    0.000 functional.py:1669(linear)
                   2229    0.202    0.000    2.459    0.001 agent.py:88(interveen)
                   2229    0.080    0.000    2.385    0.001 layers.py:17(step)
                  55725    0.158    0.000    2.297    0.000 layer.py:106(move)
                  27378    1.908    0.000    1.908    0.000 {built-in method addmm}
                 280908    0.935    0.000    1.537    0.000 tensor.py:933(grad)
                  37990    0.059    0.000    1.441    0.000 activation.py:713(forward)
                  37990    0.093    0.000    1.382    0.000 functional.py:1292(leaky_relu)
                  55725    0.307    0.000    1.373    0.000 layers.py:844(check)
                   4458    0.127    0.000    1.363    0.000 optimizer.py:167(zero_grad)
                  80244    1.315    0.000    1.315    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   2229    0.429    0.000    1.284    0.001 agent.py:67(modify)
                  37990    1.281    0.000    1.281    0.000 {built-in method torch._C._nn.leaky_relu}
                   2229    0.073    0.000    1.230    0.001 replaybuffer.py:22(sample_data)
                   2230    0.164    0.000    1.215    0.001 layers.py:793(update)
                  17299    1.139    0.000    1.139    0.000 {built-in method cat}
                   2229    0.098    0.000    0.925    0.000 replaybuffer.py:18(stacker)
                 364101    0.271    0.000    0.816    0.000 overrides.py:1070(has_torch_function)
                 455989    0.277    0.000    0.811    0.000 {built-in method builtins.any}
                   6154    0.064    0.000    0.810    0.000 agent.py:59(modify_board)
                  40122    0.793    0.000    0.793    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                  80244    0.666    0.000    0.666    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                  55725    0.136    0.000    0.643    0.000 layers.py:838(isFree)
                  15603    0.090    0.000    0.624    0.000 tensor.py:21(wrapped)
                  40122    0.593    0.000    0.593    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                  40122    0.558    0.000    0.558    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 429845    0.401    0.000    0.507    0.000 layer.py:103(isFree)
                   3925    0.149    0.000    0.437    0.000 exploration.py:53(softmaxer)
                  17840    0.252    0.000    0.428    0.000 layer.py:175(NoRock_update)
                   2229    0.222    0.000    0.381    0.000 collector.py:46(collect)
                   2229    0.025    0.000    0.363    0.000 exploration.py:47(epsilonGreedy)
                  40122    0.362    0.000    0.362    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                   4458    0.013    0.000    0.355    0.000 loss.py:445(forward)
                  40122    0.345    0.000    0.345    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   4458    0.045    0.000    0.342    0.000 functional.py:2637(mse_loss)
                   6154    0.330    0.000    0.330    0.000 {built-in method torch._C._nn.one_hot}
                  11141    0.312    0.000    0.312    0.000 {built-in method tensor}
                 771183    0.247    0.000    0.305    0.000 overrides.py:1083(<genexpr>)
                 777065    0.203    0.000    0.291    0.000 enum.py:646(__hash__)
                  55725    0.186    0.000    0.291    0.000 layers.py:246(check)
                   2229    0.091    0.000    0.282    0.000 replaybuffer.py:28(teleporter_save_data)
                  27378    0.274    0.000    0.274    0.000 {method 't' of 'torch._C._TensorBase' objects}
                  55725    0.155    0.000    0.257    0.000 layers.py:286(check)
                   2225    0.114    0.000    0.248    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                  71353    0.034    0.000    0.240    0.000 {built-in method builtins.all}
                   2541    0.083    0.000    0.233    0.000 random.py:315(sample)
                   2229    0.227    0.000    0.227    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                 500346    0.185    0.000    0.225    0.000 layers.py:809(<genexpr>)
                  21224    0.027    0.000    0.221    0.000 flatten.py:39(forward)
                   4458    0.009    0.000    0.211    0.000 game.py:38(board)
                 168156    0.064    0.000    0.203    0.000 layers.py:799(<genexpr>)
                  21224    0.194    0.000    0.194    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
          901825/901823    0.119    0.000    0.189    0.000 {built-in method builtins.len}
                   4458    0.180    0.000    0.180    0.000 {built-in method torch._C._nn.mse_loss}
                  11145    0.173    0.000    0.173    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                  40212    0.070    0.000    0.157    0.000 tensor.py:596(__hash__)
                   4458    0.156    0.000    0.156    0.000 {built-in method max}
                 135727    0.155    0.000    0.155    0.000 {built-in method torch._C._get_tracing_state}
                  13374    0.145    0.000    0.145    0.000 {built-in method sum}
                1086722    0.142    0.000    0.142    0.000 layer.py:99(positions)
                   4450    0.009    0.000    0.134    0.000 <__array_function__ internals>:2(prod)
                  55750    0.088    0.000    0.133    0.000 layers.py:113(isDone)
                  55725    0.083    0.000    0.130    0.000 layers.py:273(check)
                   3925    0.012    0.000    0.129    0.000 functional.py:1479(softmax)
                  20363    0.126    0.000    0.126    0.000 {built-in method clone}
                  55725    0.080    0.000    0.126    0.000 layers.py:313(check)
                   4450    0.008    0.000    0.124    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                  26517    0.121    0.000    0.121    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 123204    0.078    0.000    0.118    0.000 random.py:250(_randbelow_with_getrandbits)
                   3925    0.117    0.000    0.117    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                   4450    0.013    0.000    0.115    0.000 fromnumeric.py:2912(prod)
                 108112    0.115    0.000    0.115    0.000 module.py:765(__getattr__)
                   3925    0.108    0.000    0.108    0.000 {built-in method multinomial}
                  55725    0.073    0.000    0.107    0.000 layers.py:48(check)
                   4458    0.033    0.000    0.107    0.000 tensor.py:506(__rsub__)
                 139970    0.105    0.000    0.105    0.000 layer.py:154(elements)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9605553: <Test_CPU_10_0> in cluster <dcc> Done

Job <Test_CPU_10_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Sun May  2 14:24:04 2021
Job was executed on host(s) <n-62-31-24>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sun May  2 14:24:05 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  2 14:24:05 2021
Terminated at Sun May  2 14:25:11 2021
Results reported at Sun May  2 14:25:11 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   61.62 sec.
    Max Memory :                                 124 MB
    Average Memory :                             124.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16260.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   115 sec.
    Turnaround time :                            67 sec.

The output (if any) is above this job summary.

