
# Parameters

    Name :                      ReTest4-0
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        500000.0
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              1
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      37642581439 function calls (37469509580 primitive calls) in 42912.68 seconds

##    Ordered by: cumulative time
   List reduced from 510 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42912.676 42912.676 {built-in method builtins.exec}
                      1    3.544    3.544 42912.676 42912.676 <string>:1(<module>)
                      1  223.729  223.729 42909.133 42909.133 main.py:75(CFagent)
                6475410   24.475    0.000 14933.414    0.002 agent.py:29(learn)
                6473594  375.942    0.000 12127.009    0.002 learner.py:42(Qlearn)
                2158470    9.301    0.000 10001.716    0.005 game.py:41(step)
                2158470   12.752    0.000 9551.265    0.004 layers.py:718(step)
                2158470  183.914    0.000 6121.816    0.003 layers.py:17(step)
        194685766/21615598  745.994    0.000 6037.452    0.000 module.py:866(_call_impl)
              215195247  336.018    0.000 5916.929    0.000 layer.py:98(move)
                2158470  223.498    0.000 5807.196    0.003 agent.py:54(_learn)
               15142004   40.426    0.000 5606.886    0.000 network.py:24(forward)
               15142004  178.066    0.000 5468.731    0.000 container.py:117(forward)
                2158470  220.773    0.000 5327.354    0.002 agent.py:202(_learn)
                6473594   51.792    0.000 4734.485    0.001 optimizer.py:84(wrapper)
                6473594   26.353    0.000 4501.039    0.001 grad_mode.py:24(decorate_context)
                6473594  191.166    0.000 4416.565    0.001 adam.py:55(step)
                6473594  929.382    0.000 4013.209    0.001 _functional.py:53(adam)
                2158470   61.219    0.000 3761.855    0.002 agent.py:117(_learn)
              215195247  724.259    0.000 3448.383    0.000 layers.py:735(check)
                2158471  301.631    0.000 3397.136    0.002 layers.py:684(update)
                2158470  366.555    0.000 3383.394    0.002 agent.py:210(counterfact)
                2158470 2549.622    0.001 3191.845    0.001 replaybuffer.py:22(sample_data)
                6473594   24.855    0.000 3158.816    0.000 tensor.py:195(backward)
                6473594   24.565    0.000 3133.099    0.000 __init__.py:68(backward)
                6473594 2986.286    0.000 2986.286    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2158470 2058.808    0.001 2677.176    0.001 replaybuffer.py:52(sample_data)
                4330944  108.371    0.000 2659.721    0.001 agent.py:49(__call__)
                2158470 1128.802    0.001 2440.776    0.001 agent.py:88(interveen)
               28762036 2426.433    0.000 2426.433    0.000 {built-in method tensor}
               23841242   14.275    0.000 2309.795    0.000 game.py:37(board)
                2158470 1251.678    0.001 2203.168    0.001 replaybuffer.py:28(teleporter_save_data)
               34535528 1153.722    0.000 2069.186    0.000 layer.py:167(NoRock_update)
               30284008   66.612    0.000 2054.452    0.000 conv.py:398(forward)
               30284008   44.377    0.000 1955.804    0.000 conv.py:390(_conv_forward)
               30284008 1911.427    0.000 1911.427    0.000 {built-in method conv2d}
              215195247  328.369    0.000 1830.236    0.000 layers.py:729(isFree)
               41109072   80.552    0.000 1529.672    0.000 linear.py:93(forward)
                2158470 1001.818    0.000 1510.081    0.001 agent.py:67(modify)
             1492629085 1270.357    0.000 1501.867    0.000 layer.py:95(isFree)
               41109072   33.463    0.000 1406.318    0.000 functional.py:1737(linear)
               41109072 1364.475    0.000 1364.475    0.000 {built-in method torch._C._nn.linear}
               28065034 1015.007    0.000 1015.007    0.000 {built-in method cat}
              101616400  930.106    0.000  930.106    0.000 {built-in method clone}
                2156654   36.372    0.000  916.099    0.000 agent.py:171(__call__)
                2158470   34.850    0.000  873.498    0.000 agent.py:112(__call__)
               56251076   43.856    0.000  801.467    0.000 activation.py:713(forward)
                6489414   38.405    0.000  800.786    0.000 agent.py:59(modify_board)
              120838000  782.271    0.000  782.271    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             3060989244  531.958    0.000  763.864    0.000 enum.py:646(__hash__)
               56251076   44.680    0.000  757.612    0.000 functional.py:1364(leaky_relu)
              215195247  487.040    0.000  754.251    0.000 layers.py:286(check)
              215778746  176.092    0.000  746.322    0.000 {built-in method builtins.any}
               56251076  703.904    0.000  703.904    0.000 {built-in method torch._C._nn.leaky_relu}
                2158470  544.035    0.000  695.909    0.000 replaybuffer.py:58(CF_save_data)
                6473594  122.322    0.000  695.809    0.000 optimizer.py:189(zero_grad)
                2226825   23.762    0.000  693.713    0.000 layers.py:740(restart)
              120838000  693.179    0.000  693.179    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              215195247  388.699    0.000  654.321    0.000 layers.py:246(check)
             1922582475  470.786    0.000  570.230    0.000 layers.py:700(<genexpr>)
                6489414  530.104    0.000  530.104    0.000 {built-in method torch._C._nn.one_hot}
              680301079  526.668    0.000  526.668    0.000 layer.py:146(elements)
              215847100   79.807    0.000  509.545    0.000 {built-in method builtins.all}
                2158470   38.274    0.000  490.173    0.000 replaybuffer.py:18(stacker)
                2226825   12.234    0.000  489.690    0.000 level.py:8(__init__)
                2156654   34.641    0.000  471.744    0.000 replaybuffer.py:48(stacker)
              932775541  227.455    0.000  453.925    0.000 layers.py:690(<genexpr>)
               60419000  451.359    0.000  451.359    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               60419000  397.166    0.000  397.166    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2226825   47.332    0.000  383.631    0.000 levels.py:164(generate)
               60419000  376.374    0.000  376.374    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               60419000  367.500    0.000  367.500    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             3919803130  349.756    0.000  349.756    0.000 layer.py:91(positions)
        4758576872/4758576869  299.105    0.000  336.689    0.000 {built-in method builtins.len}
                8770590  126.984    0.000  332.468    0.000 random.py:315(sample)
              422933084  267.678    0.000  331.640    0.000 tensor.py:906(grad)
              215195247  205.879    0.000  331.271    0.000 layers.py:273(check)
              215195247  202.491    0.000  322.447    0.000 layers.py:313(check)
                2158470  181.302    0.000  306.582    0.000 collector.py:46(collect)
                4453650   40.093    0.000  277.533    0.000 level.py:41(notUsed)
              215195247  187.689    0.000  276.839    0.000 layers.py:48(check)
               60419000  275.932    0.000  275.932    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4330944   99.289    0.000  271.804    0.000 exploration.py:53(softmaxer)
                6473594    9.624    0.000  263.938    0.000 loss.py:527(forward)
                2158470   45.294    0.000  260.163    0.000 agent.py:277(counterfact_check)
                6473594   24.167    0.000  254.314    0.000 functional.py:2898(mse_loss)
             3061014027  231.910    0.000  231.910    0.000 {built-in method builtins.hash}
              215195247  146.417    0.000  220.341    0.000 layers.py:23(check)
              110262468  211.521    0.000  211.521    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               17814600   22.303    0.000  174.286    0.000 layer.py:69(restart)
              272063100  112.780    0.000  165.579    0.000 random.py:250(_randbelow_with_getrandbits)
              306296083  120.679    0.000  165.105    0.000 layer.py:130(add)
              193086925  103.655    0.000  155.630    0.000 layer.py:126(remove)
                6473594  155.273    0.000  155.273    0.000 {built-in method torch._C._nn.mse_loss}
               15109290  152.742    0.000  152.742    0.000 {built-in method sum}
             1951968614  147.933    0.000  147.933    0.000 {method 'random' of '_random.Random' objects}
                4316942  143.946    0.000  143.946    0.000 {built-in method nonzero}
                6474242  141.188    0.000  141.188    0.000 {built-in method max}
               30284008   20.761    0.000  135.632    0.000 flatten.py:39(forward)
               34535528  127.817    0.000  127.817    0.000 layer.py:178(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9512495: <ReTest4_0> in cluster <dcc> Done

Job <ReTest4_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 13 13:40:47 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 13 20:47:39 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 20:47:39 2021
Terminated at Wed Apr 14 08:42:58 2021
Results reported at Wed Apr 14 08:42:58 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   42807.46 sec.
    Max Memory :                                 7410 MB
    Average Memory :                             5372.26 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8974.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42919 sec.
    Turnaround time :                            68531 sec.

The output (if any) is above this job summary.

