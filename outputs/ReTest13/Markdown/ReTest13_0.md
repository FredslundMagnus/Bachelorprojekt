
# Parameters

    Name :                      ReTest13-0
    Main :                      CFagent
    Level :                     Levels.Coconuts
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      66943071252 function calls (66645218417 primitive calls) in 86108.44 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86108.442 86108.442 {built-in method builtins.exec}
                      1    4.138    4.138 86108.442 86108.442 <string>:1(<module>)
                      1  445.692  445.692 86104.304 86104.304 main.py:75(CFagent)
               11166609   54.539    0.000 29055.372    0.003 agent.py:29(learn)
               11165422  750.471    0.000 23360.412    0.002 learner.py:42(Qlearn)
                3722203   18.903    0.000 22857.151    0.006 game.py:41(step)
                3722203   24.664    0.000 22019.782    0.006 layers.py:718(step)
                3722203  386.588    0.000 15470.082    0.004 layers.py:17(step)
              372065073 1472.242    0.000 15049.586    0.000 layer.py:98(move)
        335078229/37227085 1489.891    0.000 11719.664    0.000 module.py:866(_call_impl)
                3722203  454.326    0.000 11321.639    0.003 agent.py:54(_learn)
               26061663   75.273    0.000 10816.895    0.000 network.py:24(forward)
               26061663  357.771    0.000 10549.270    0.000 container.py:117(forward)
                3722203  446.444    0.000 10358.711    0.003 agent.py:202(_learn)
              372065073 1469.570    0.000 9174.014    0.000 layers.py:735(check)
               11165422  108.474    0.000 8954.005    0.001 optimizer.py:84(wrapper)
               11165422   60.685    0.000 8489.698    0.001 grad_mode.py:24(decorate_context)
               11165422  394.984    0.000 8297.840    0.001 adam.py:55(step)
               11165422 1731.475    0.000 7501.062    0.001 _functional.py:53(adam)
                3722203  113.316    0.000 7290.735    0.002 agent.py:117(_learn)
                3722203 5706.567    0.002 6953.550    0.002 replaybuffer.py:22(sample_data)
                3722204  580.785    0.000 6486.778    0.002 layers.py:684(update)
               11165422   46.895    0.000 6237.601    0.001 tensor.py:195(backward)
               11165422   54.186    0.000 6188.985    0.001 __init__.py:68(backward)
                3722203 4853.679    0.001 6055.545    0.002 replaybuffer.py:52(sample_data)
               11165422 5886.554    0.001 5886.554    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7438494  228.307    0.000 5309.937    0.001 agent.py:49(__call__)
                3722203  357.920    0.000 4938.256    0.001 agent.py:210(counterfact)
                3722203 2214.017    0.001 4786.493    0.001 agent.py:88(interveen)
                3722203 2437.089    0.001 4134.946    0.001 replaybuffer.py:28(teleporter_save_data)
               52123326  124.660    0.000 3971.836    0.000 conv.py:398(forward)
               52110849 2306.400    0.000 3916.574    0.000 layer.py:151(update)
               52123326   84.025    0.000 3781.616    0.000 conv.py:390(_conv_forward)
               52123326 3697.591    0.000 3697.591    0.000 {built-in method conv2d}
               43497234 3590.011    0.000 3590.011    0.000 {built-in method tensor}
              372065073  593.287    0.000 3400.392    0.000 layers.py:729(isFree)
               34967155   22.699    0.000 3360.245    0.000 game.py:37(board)
              372065073 2205.619    0.000 3023.805    0.000 layers.py:471(check)
               70740583  148.184    0.000 2928.941    0.000 linear.py:93(forward)
                3722203 1885.336    0.001 2903.296    0.001 agent.py:67(modify)
             2513018180 2407.404    0.000 2807.105    0.000 layer.py:95(isFree)
               70740583   62.463    0.000 2696.410    0.000 functional.py:1737(linear)
               70740583 2619.607    0.000 2619.607    0.000 {built-in method torch._C._nn.linear}
              372065073 1756.222    0.000 2368.428    0.000 layers.py:77(check)
               48376792 1945.112    0.000 1945.112    0.000 {built-in method cat}
                3721016   77.160    0.000 1843.398    0.000 agent.py:171(__call__)
             6504046649 1209.109    0.000 1749.129    0.000 enum.py:646(__hash__)
                3722203   72.538    0.000 1650.982    0.000 agent.py:112(__call__)
               11160697   84.457    0.000 1609.154    0.000 agent.py:59(modify_board)
              155618291 1540.943    0.000 1540.943    0.000 {built-in method clone}
               96802246   87.361    0.000 1526.725    0.000 activation.py:713(forward)
              208419628 1451.010    0.000 1451.010    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               96802246   87.263    0.000 1439.364    0.000 functional.py:1364(leaky_relu)
              374478389  308.914    0.000 1376.928    0.000 {built-in method builtins.any}
               96802246 1335.753    0.000 1335.753    0.000 {built-in method torch._C._nn.leaky_relu}
                1464215   20.428    0.000 1331.868    0.001 layers.py:740(restart)
              208419628 1290.660    0.000 1290.660    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11165422  236.295    0.000 1280.391    0.000 optimizer.py:189(zero_grad)
                1464215    9.668    0.000 1155.863    0.001 level.py:8(__init__)
               11160697 1074.149    0.000 1074.149    0.000 {built-in method torch._C._nn.one_hot}
             2966049480  878.633    0.000 1068.014    0.000 layers.py:700(<genexpr>)
                1464215   71.019    0.000 1066.806    0.001 levels.py:262(generate)
              372065073  814.425    0.000 1038.687    0.000 layers.py:62(check)
             1019660559  953.134    0.000  953.134    0.000 layer.py:146(elements)
                3722203   69.050    0.000  939.445    0.000 replaybuffer.py:18(stacker)
               16660154  158.796    0.000  930.927    0.000 level.py:41(notUsed)
              372220400   73.577    0.000  924.660    0.000 {built-in method builtins.all}
                3721016   68.153    0.000  905.131    0.000 replaybuffer.py:48(stacker)
              772057780  183.066    0.000  899.108    0.000 layers.py:690(<genexpr>)
                3722203  746.873    0.000  895.356    0.000 replaybuffer.py:58(CF_save_data)
              104209814  846.746    0.000  846.746    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             8744907278  821.522    0.000  821.522    0.000 layer.py:91(positions)
              104209814  753.703    0.000  753.703    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              372220400  486.717    0.000  703.708    0.000 layers.py:113(isDone)
              104209814  699.000    0.000  699.000    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              104209814  697.521    0.000  697.521    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              729468782  493.813    0.000  610.928    0.000 tensor.py:906(grad)
        7419792929/7419792926  523.953    0.000  597.599    0.000 {built-in method builtins.len}
                7444406  218.793    0.000  590.908    0.000 random.py:315(sample)
                3722203  341.987    0.000  579.545    0.000 collector.py:46(collect)
                7438494  198.175    0.000  577.898    0.000 exploration.py:53(softmaxer)
              372065073  378.058    0.000  555.376    0.000 layers.py:48(check)
               11165422   21.317    0.000  553.285    0.000 loss.py:527(forward)
             6504089016  540.029    0.000  540.029    0.000 {built-in method builtins.hash}
               11165422   55.609    0.000  531.968    0.000 functional.py:2898(mse_loss)
                3722203   90.753    0.000  515.109    0.000 agent.py:277(counterfact_check)
              104209814  501.264    0.000  501.264    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              372065073  289.014    0.000  420.881    0.000 layers.py:23(check)
               16660154   13.637    0.000  416.046    0.000 level.py:38(elementsIn)
              170500004  372.858    0.000  372.858    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              376097519  230.198    0.000  359.070    0.000 layer.py:126(remove)
               11165422  323.312    0.000  323.312    0.000 {built-in method torch._C._nn.mse_loss}
                7444408  293.408    0.000  293.408    0.000 {built-in method nonzero}
               11166537  292.928    0.000  292.928    0.000 {built-in method max}
               26055421  292.286    0.000  292.286    0.000 {built-in method sum}
              458003551  202.919    0.000  282.097    0.000 layer.py:130(add)
             2513018180  274.682    0.000  274.682    0.000 layer.py:203(isBlocking)
               16660154  132.427    0.000  266.078    0.000 level.py:39(<listcomp>)
              389693333  178.543    0.000  263.486    0.000 random.py:250(_randbelow_with_getrandbits)
             2984120217  263.044    0.000  263.044    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9515520: <ReTest13_0> in cluster <dcc> Done

Job <ReTest13_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 14 15:03:58 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 14 15:05:39 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 14 15:05:39 2021
Terminated at Thu Apr 15 15:00:53 2021
Results reported at Thu Apr 15 15:00:53 2021

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

    CPU time :                                   85904.55 sec.
    Max Memory :                                 10484 MB
    Average Memory :                             6809.20 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5900.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86117 sec.
    Turnaround time :                            86215 sec.

The output (if any) is above this job summary.

